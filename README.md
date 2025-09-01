# Kurulum
1. Repo Klonlama
```bash
git clone https://github.com/kelma01/clinique
```

2. Python Virtual Environment Kurulum
```bash
python -m venv venv
```

3. Venv'i Aktive Etme
```bash
Set-ExecutionPolicy Unrestricted -Scope Process #izinlerin tanımlanması
.\venv\Scripts\activate
```

4. Proje Klasörüne Gitme
```bash
cd clinique
```

5. Gereksinimlerin İndirilmesi
```bash
pip install -r requirements.txt
```

6. Static Dosyaların Yüklenmesi
```bash
py ./manage.py collectstatic
```

7. Server'in ayağa kaldırılması
```bash
py .\manage.py runserver
```
