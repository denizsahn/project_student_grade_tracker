from storage import load_state, save_state
from roster import add_student
from grades import record_grade

DATA_DIR = "data"  # Verilerin okunacağı ve yazılacağı klasör yolunu bir sabit değişkene atar


def main():  # Ana program akışını yönetecek fonksiyonu tanımlar
    students, courses, gradebook, settings = load_state(DATA_DIR)  

    
    student = {"id": "S001", "name": "Alice", "email": "alice@school.edu"}  # Test için örnek bir öğrenci verisi (sözlük şeklinde) oluşturur
    add_student(students, student)  # Oluşturulan bu öğrenciyi mevcut öğrenci listesine ekler

    assessment = {  # Bir sınav veya ödev değerlendirmesi için veri yapısı oluşturur
        "id": "A1",        # Değerlendirme kimliği
        "name": "Midterm", # Değerlendirme adı (Vize)
        "score": 85,       # Alınan puan
        "weight": 100      # Ağırlık/Tam puan
    }

    record_grade(gradebook, "CS101", "S001", assessment)  # CS101 dersi ve S001 ID'li öğrenci için notu not defterine işler

    save_state(DATA_DIR, students, courses, gradebook, settings)  # Yapılan tüm değişiklikleri (yeni öğrenci, not vb.) dosyaya geri kaydeder
    print("System state saved successfully.")  # İşlemin başarıyla tamamlandığını ekrana yazdırır


if __name__ == "__main__":  # Eğer bu dosya ana program olarak çalıştırılıyorsa (başka yerden import edilmediyse)
    main()  # main fonksiyonunu çalıştırır

