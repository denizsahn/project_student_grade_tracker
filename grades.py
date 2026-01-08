def record_grade(gradebook: dict, course_id: str, student_id: str, assessment: dict) -> dict:  # Yeni not kaydetmek için fonksiyon tanımı
    gradebook.setdefault(course_id, {})  # Kurs sözlükte yoksa boş olarak oluşturur
    gradebook[course_id].setdefault(student_id, {})  # Öğrenci kursta yoksa boş olarak oluşturur

    assessment_id = assessment["id"]  # Değerlendirme ID'sini değişkene atar
    if assessment_id in gradebook[course_id][student_id]:  # Bu ID daha önce kaydedilmiş mi kontrol eder
        raise ValueError("Duplicate assessment ID")  # Eğer varsa hata fırlatır

    if not 0 <= assessment["score"] <= 100:  # Puanın 0-100 arasında olup olmadığını kontrol eder
        raise ValueError("Score must be between 0 and 100")  # Aralık dışındaysa hata verir

    gradebook[course_id][student_id][assessment_id] = assessment  # Notu ilgili yere kaydeder
    return gradebook  # Güncellenmiş not defterini döndürür


def update_grade(gradebook: dict, course_id: str, student_id: str, assessment_id: str, new_score: float) -> dict:  # Mevcut bir notu güncelleme fonksiyonu
    if not 0 <= new_score <= 100:  # Yeni puanın geçerliliğini kontrol eder
        raise ValueError("Invalid score")  # Geçersizse hata verir

    gradebook[course_id][student_id][assessment_id]["score"] = new_score  # İlgili sınavın puanını günceller
    return gradebook  # Güncel sözlüğü döndürür


def delete_grade(gradebook: dict, course_id: str, student_id: str, assessment_id: str) -> dict:  # Not silme fonksiyonu
    del gradebook[course_id][student_id][assessment_id]  # Belirtilen sınavı sözlükten siler
    return gradebook  # Güncel sözlüğü döndürür


def calculate_student_average(gradebook: dict, course_id: str, student_id: str) -> float:  # Öğrenci ortalamasını hesaplama fonksiyonu
    scores = gradebook.get(course_id, {}).get(student_id, {}).values()  # Öğrencinin tüm sınav bilgilerini çeker
    if not scores:  # Eğer hiç not yoksa
        return 0.0  # Ortalamayı 0 returnler

    total_weight = sum(a["weight"] for a in scores)  # Tüm sınavların ağırlıklarını toplar
    if total_weight != 100:  # Ağırlık toplamı 100 değilse
        raise ValueError("Weights must sum to 100")  # Hata verir

    return sum(a["score"] * a["weight"] / 100 for a in scores)  # Ağırlıklı ortalamayı hesaplayıp döndürür


def calculate_course_average(gradebook: dict, course_id: str) -> float:  # Kurs genel ortalamasını hesaplama fonksiyonu
    students = gradebook.get(course_id, {})  # Kurstaki tüm öğrencileri alır
    if not students:  
        return 0.0  

    averages = [  # Tüm öğrencilerin ortalamalarını içeren bir liste oluşturur
        calculate_student_average(gradebook, course_id, sid)  # Her öğrenci için ortalama hesaplar
        for sid in students  # Öğrenci ID'leri üzerinde döner
    ]
    return sum(averages) / len(averages)  # Ortalamaların aritmetik ortalamasını alır


def set_grade_policy(course_settings: dict, course_id: str, policy: dict) -> dict:  # Notlandırma politikası belirleme fonksiyonu
    course_settings[course_id] = policy  # Kurs için politikayı (katsayıları vb.) kaydeder
    return course_settings 


def compute_weighted_score(scores: list[dict], policy: dict) -> float:  # Kategori bazlı ağırlıklı puan hesaplama
    total = 0  # Toplam puanı tutacak değişken
    for s in scores:  
        category = s["category"]  # Sınavın kategorisini (vize, final vb.) alır
        total += s["score"] * policy[category] / 100  # Politikadaki katsayıya göre puanı ekler
    return total  #


def assign_letter_grade(score: float, scale: dict) -> str:  # Puana göre harf notu belirleme
    for letter, threshold in scale.items():  # Harf ve eşik değerleri üzerinde döner
        if score >= threshold:  # Puan eşiği geçiyorsa
            return letter  
    return "F"  # Hiçbir eşiği geçemezse F döndürür
