from . import db
from datetime import datetime
from flask_login import UserMixin # Kullanıcı giriş işlemleri için gerekli standart# --- 1. KATEGORİ TABLOSU (Category) ---
# Yazıların türünü tutar (Teknoloji, Spor, Günlük vb.)
class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    
    # İlişki: Bir kategorinin birden fazla yazısı olabilir
    posts = db.relationship('Post', backref='category', lazy=True)    
    def __repr__(self):
        return f"<Category {self.name}>"# --- 2. KULLANICI TABLOSU (User) ---
# UserMixin: Flask-Login'in kullanıcıyı tanıması için gerekli metotları sağlar
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False) # Hashlenmiş şifre
    
    # İlişkiler
    posts = db.relationship('Post', backref='author', lazy=True)
    comments = db.relationship('Comment', backref='author', lazy=True)
    likes = db.relationship('PostLike', backref='user', lazy=True)    
    def __repr__(self):
        return f"<User {self.username}>"# --- 3. YAZI TABLOSU (Post) ---
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    content = db.Column(db.Text, nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    
    # Ayarlar
    allow_comments = db.Column(db.Boolean, default=True, nullable=False)
    
    # Foreign Keys (Dış Anahtarlar)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=True) # Kategori silinirse yazı kalsın (nullable=True)    # İlişkiler
    comments = db.relationship('Comment', backref='post', lazy=True, cascade="all, delete-orphan")
    likes = db.relationship('PostLike', backref='post', lazy=True, cascade="all, delete-orphan")    
    def __repr__(self):
        return f"<Post {self.title}>"# --- 4. YORUM TABLOSU (Comment) ---
class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.Text, nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    
    # Bağlantılar
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)# --- 5. BEĞENİ TABLOSU (PostLike) ---
# Çoka-Çok ilişki yerine normalize edilmiş ara tablo
class PostLike(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=False)    # Constraint: Bir kullanıcı aynı postu sadece 1 kere beğenebilir
    __table_args__ = (db.UniqueConstraint('user_id', 'post_id', name='unique_user_post_like'),)