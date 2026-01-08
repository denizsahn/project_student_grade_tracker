import json 
import os  # İşletim sistemi işlemleri (dosya yolu, klasör oluşturma vb.) için
import shutil  # Dosya ve klasör kopyalama işlemleri için
from datetime import datetime  # Tarih ve saat bilgisi almak için


def load_state(base_dir: str):
    # Ensure data directory exists
    os.makedirs(base_dir, exist_ok=True)  # Ana veri klasörü yoksa oluştur, varsa hata verme

    # Helper function to load JSON safely
    def load_json(path, default):
        if not os.path.exists(path):  # Belirtilen dosya var mı kontrol et
            return default  # Dosya yoksa varsayılan boş değeri (örneğin []) döndür
        with open(path, "r") as f:  # Dosyayı okuma modunda ('r') aç
            return json.load(f)  # Dosyadaki JSON verisini Python nesnesine çevirip döndür

    students = load_json(os.path.join(base_dir, "students.json"), [])  # Öğrenci listesini yükle, yoksa boş liste dön
    courses = load_json(os.path.join(base_dir, "courses.json"), [])  # Ders listesini yükle, yoksa boş liste dön
    gradebook = load_json(os.path.join(base_dir, "grades.json"), {})  # Not defterini yükle, yoksa boş sözlük dön
    settings = load_json(os.path.join(base_dir, "settings.json"), {})  # Ayarları yükle, yoksa boş sözlük dön

    return students, courses, gradebook, settings  # Yüklenen tüm verileri topluca geri döndür


def save_state(base_dir: str, students: list, courses: list, gradebook: dict, settings: dict):
    os.makedirs(base_dir, exist_ok=True)  # Kayıt yapılacak klasörün varlığından emin ol

    # Save each component into its own JSON file
    with open(os.path.join(base_dir, "students.json"), "w") as f:  # Öğrenci dosyasını yazma modunda ('w') aç
        json.dump(students, f, indent=2)  # Öğrenci verisini girintili (okunaklı) şekilde dosyaya yaz

    with open(os.path.join(base_dir, "courses.json"), "w") as f:  # Ders dosyasını yazma modunda aç
        json.dump(courses, f, indent=2)  # Ders verisini dosyaya yaz

    with open(os.path.join(base_dir, "grades.json"), "w") as f:  # Not dosyasını yazma modunda aç
        json.dump(gradebook, f, indent=2)  # Not verisini dosyaya yaz

    with open(os.path.join(base_dir, "settings.json"), "w") as f:  # Ayar dosyasını yazma modunda aç
        json.dump(settings, f, indent=2)  # Ayar verisini dosyaya yaz


def backup_state(base_dir: str, backup_dir: str):
    os.makedirs(backup_dir, exist_ok=True)  # Yedekleme klasörünü oluştur (varsa hata verme)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")  # Şu anki zamanı dosya isminde kullanmak için formatla
    backup_path = os.path.join(backup_dir, f"backup_{timestamp}")  # Yedek klasörünün tam yolunu belirle

    shutil.copytree(base_dir, backup_path)  # Ana veri klasörünü tüm içeriğiyle yedek yoluna kopyala
    return [backup_path]  


def import_from_csv(csv_path: str, course_id: str):
    import csv  # CSV okuma modülünü sadece bu
