# 🚀 BLOG3 - Modern Blog Platformu

**BLOG3**, kullanıcıların düşüncelerini özgürce paylaşabileceği, kategorize edilmiş içerikleri keşfedebileceği ve toplulukla etkileşime geçebileceği, Python ve Flask altyapısı ile geliştirilmiş modern bir MVP (Minimum Viable Product) blog projesidir.

## 📋 İçindekiler

- [Proje Hakkında]
    
- [Özellikler]
    
- [Teknoloji Yığını]
    
- [Sistem Mimarisi ve Akış]
    
- [Kurulum ve Çalıştırma]
    
- [Proje Yapısı]
    
- [Ekran Görüntüleri]
    
- [Ekip]
    

---

## 📖 Proje Hakkında

Bu proje, web geliştirme süreçlerini (Backend, Frontend, Veritabanı) uçtan uca deneyimlemek ve temiz kod mimarisine (Factory Pattern, MVC) uygun, ölçeklenebilir bir web uygulaması ortaya koymak amacıyla geliştirilmiştir. Kullanıcı dostu arayüzü ve güçlü backend yapısı ile güvenli ve hızlı bir blog deneyimi sunar.

---

## ✨ Özellikler

- **Güvenli Kimlik Doğrulama:** Kullanıcı kayıt ve giriş işlemleri (Parola hashleme ile güvenli saklama).
    
- **CRUD İşlemleri:** Blog yazısı oluşturma, okuma, güncelleme ve silme.
    
- **Kategori Sistemi:** Yazıları belirli konulara göre filtreleme.
    
- **Etkileşim:** AJAX tabanlı (sayfa yenilenmeden) beğeni ve yorum sistemi.
    
- **Gelişmiş Arama:** Başlık ve içerik bazlı dinamik arama.
    
- **Responsive Tasarım:** Mobil ve masaüstü uyumlu modern arayüz.
    

---

## 🛠 Teknoloji Yığını

|**Alan**|**Teknolojiler**|
|---|---|
|**Backend**|Python, Flask, Flask-Login, Werkzeug|
|**Veritabanı**|SQLite, SQLAlchemy (ORM), Flask-Migrate|
|**Frontend**|HTML5, CSS3, JavaScript (AJAX), Jinja2 Template Engine|
|**Versiyon Kontrol**|Git & GitHub|

---

## 🏗 Sistem Mimarisi ve Akış

Projemiz, kullanıcı deneyimini merkeze alan bir akış şemasına sahiptir. Aşağıdaki diyagramda sayfa geçişleri ve kullanıcı yetkileri görselleştirilmiştir:

- **Ziyaretçi:** Ana sayfayı görüntüler, arama yapar.
    
- **Üye:** Giriş yapar, yazı yazar, yorum yapar ve beğeni gönderir.
    

---

## ⚙️ Kurulum ve Çalıştırma

Projeyi yerel makinenizde çalıştırmak için aşağıdaki adımları izleyin:

1. **Repoyu Klonlayın:**
    
    
    ```Bash
    git clone https://github.com/KullaniciAdiniz/BLOG3.git
    cd BLOG3
    ```
    
2. **Sanal Ortamı Oluşturun ve Aktif Edin:**
    
    
    
    ```Bash
    python -m venv venv
    # Windows için:
    venv\Scripts\activate
    # Mac/Linux için:
    source venv/bin/activate
    ```
    
3. **Gereksinimleri Yükleyin:**
    
    
    
    ```Bash
    pip install -r requirements.txt
    ```
    
4. **Veritabanını Oluşturun:**
    
    
    
    ``` Bash
    # Örnek verilerle veritabanını kurmak için (varsa)
    python seed_data.py
    # Veya manuel kurulum için
    flask db upgrade
    ```
    
5. **Uygulamayı Başlatın:**
    
    
    
    ```Bash
    python run.py
    ```
    
    Tarayıcınızda `http://127.0.0.1:5000` adresine gidin.
    

---

## 📂 Proje Yapısı

Projemiz **Factory Pattern** yapısına uygun olarak modüler bir şekilde tasarlanmıştır. Dosya ağacımız şu şekildedir:

- `app/`: Uygulamanın ana modülü (Modeller, Rotalar, Formlar).
    
- `app/templates/`: HTML şablon dosyaları.
    
- `app/static/`: CSS, JavaScript ve resim dosyaları.
    
- `instance/`: SQLite veritabanı dosyası (`blog.db`).
    
- `run.py`: Uygulamayı başlatan giriş noktası.
    

---

## 📸 Ekran Görüntüleri

### 1. Ana Sayfa

![Uploading Screenshot 2026-02-04 at 11.57.41.png…]()


### 2. Yazı Oluşturma Paneli

<img width="1860" height="977" alt="yazi alani" src="https://github.com/user-attachments/assets/b246a864-036f-4be0-a885-da5c3107381c" />

---

## 👥 Ekip

Bu proje aşağıdaki ekip üyeleri tarafından geliştirilmiştir:

- **Veritabanı:** Emirhan & Oğuz
    
- **Backend:** Damla & Kadir
    
- **Frontend:** Muhammed & Zeynep Tuba
    

---

Tüm hakları saklıdır © 2026 BLOG3
