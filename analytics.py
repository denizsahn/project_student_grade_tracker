def grade_distribution(gradebook: dict, course_id: str, bins: list[int]) -> dict:  # Not defteri, kurs kimliği ve aralık listesini alıp bir sözlük tanımlar.
    distribution = {f"{bins[i]}-{bins[i+1]}": 0 for i in range(len(bins) - 1)}  # Aralık listesine göre anahtarlar oluşturur ve değerlerini 0 yapar

    for student_id in gradebook.get(course_id, {}):  # Her öğrenci kimliği için döngü başlatır, kurs yoksa boş output çıkarır
        avg = sum(  # Öğrencinin not ortalamasını hesaplamak için 
            a["score"] * a["weight"] / 100  # Puanı ağırlıkla çarpıp 100'e bölerek ağırlıklı puanı bulur (not ort.)
            for a in gradebook[course_id][student_id].values() 
        )  
        for i in range(len(bins) - 1):  # Not aralıkları (bins) listesinin uzunluğuna göre bir döngü 
            if bins[i] <= avg < bins[i + 1]:  # Ortalamanın belirtilen aralıkta olup olmadığına bakar
                distribution[f"{bins[i]}-{bins[i+1]}"] += 1  # Eğer aralığa uyuyorsa, o aralıktaki öğrenci sayısını 1 artırır

    return distribution  # Hangi aralıkta kaç öğrenci olduğunu gösteren dağılım sözlüğünü döndürür


def top_performers(gradebook: dict, course_id: str, limit: int = 5) -> list:  # En başarılı öğrencileri bulan fonksiyon, limit verilmezse 5'tir
    averages = []  # Öğrenci kimliklerini ve ortalamalarını tutacak bir boş liste oluşturur
    for student_id in gradebook.get(course_id, {}):  
        avg = sum(  # Öğrencinin toplam ağırlıklı ortalamasını hesaplar
            a["score"] * a["weight"] / 100  # Tek bir değerlendirmenin ağırlıklı puanını hesaplar
            for a in gradebook[course_id][student_id].values()  # Bu öğrenciye ait tüm değerlendirmeleri döngüler
        ) 
        averages.append((student_id, avg))  # Öğrenci kimliğini ve hesaplanan ortalamayı bir tuple olarak listeye ekler

    averages.sort(key=lambda x: x[1], reverse=True)  # Listeyi not ortalamasına göre büyükten küçüğe sıralar
    return averages[:limit]  # Listenin başından limit sayısı kadar (en yüksek puanlı) öğrenciyi döndürür


def student_progress_report(gradebook: dict, course_id: str, student_id: str) -> dict:  # Belirli bir öğrenci için özet rapor sözlüğü oluşturan fonksiyon
    assessments = gradebook.get(course_id, {}).get(student_id, {})  # Öğrencinin değerlendirmelerini çeker; kurs veya öğrenci yoksa boş sözlük döner
    completed = len(assessments)  # Sözlükteki eleman sayısına bakarak tamamlanan değerlendirme sayısını bulur

    average = sum(  # Eğer değerlendirme varsa ağırlıklı ortalamayı hesaplar
        a["score"] * a["weight"] / 100 for a in assessments.values()  # Her bir değerlendirme için ağırlıklı puanı hesaplayan üreteç
    ) if assessments else 0  # Eğer assessments doluysa hesaplar, boşsa ortalamayı 0 kabul eder

    return {  # Özet verileri içeren bir sözlük döndürür
        "student_id": student_id,  # Öğrencinin kimlik bilgisi
        "completed_assessments": completed,  # Tamamlanan değerlendirme sayısı
        "current_average": average  # Hesaplanan mevcut ağırlıklı ortalama
    } 


def export_report(report: dict, filename: str) -> str:  # Rapor dict'ini bir dosyaya kaydetmek için fonksiyon tanımlar
    import json  
    with open(filename, "w") as f:  # Dosyayı yazma ("w") modunda açar, işlem bitince dosya otomatik kapanır
        json.dump(report, f, indent=2)  # Raporu dosyaya JSON formatında, 2 boşluklu girintilerle yazar
    return filename  # Oluşturulan dosyanın adını geri döndürür
