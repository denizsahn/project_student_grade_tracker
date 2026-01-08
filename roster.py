def load_students(path: str) -> list:
    import json  
    try:
        with open(path, "r") as f:  # Dosyayı okuma modunda güvenli şekilde açar
            return json.load(f)  # Dosyadaki veriyi okuyup liste olarak döndürür
    except FileNotFoundError:  # Eğer dosya bulunamazsa hatayı yakalar
        return []  # Dosya yoksa boş bir liste döndürür

def save_students(path: str, students: list) -> None:
    import json 
    with open(path, "w") as f:  # Dosyayı yazma modunda güvenli şekilde açar
        json.dump(students, f, indent=2)  # Listeyi dosyaya JSON formatında yazar

def add_student(students: list, student_data: dict) -> dict:
    students.append(student_data)  # Öğrenci verisini (sözlük) listeye ekler
    return student_data  

def update_student(students: list, student_id: str, updates: dict) -> dict:
    for student in students:  # Öğrenci listesindeki her öğrenciyi tek tek gezer
        if student["id"] == student_id:  # Eğer öğrencinin ID'si aranan ID ile eşleşirse
            student.update(updates)  # Öğrenci bilgilerini yeni verilerle günceller
            return student  # Güncellenmiş öğrenciyi döndürür ve fonksiyondan çıkar
    raise ValueError("Student not found")  # Döngü biterse ve öğrenci bulunamazsa hata verir

def enroll_student(course_roster: dict, student_id: str) -> dict:
    course_roster.setdefault("students", [])  # students anahtarı yoksa oluşturur, varsa dokunmaz
    if student_id not in course_roster["students"]:  # Eğer öğrenci zaten listede yoksa
        course_roster["students"].append(student_id)  # Öğrenci ID'sini listeye ekler
    return course_roster  

def withdraw_student(course_roster: dict, student_id: str) -> dict:
    if student_id in course_roster.get("students", []):  # Öğrenci listede var mı diye kontrol eder
        course_roster["students"].remove(student_id)  # Varsa öğrenci ID'sini listeden siler
    return course_roster  
