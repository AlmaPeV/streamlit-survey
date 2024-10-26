import firebase_admin
from firebase_admin import credentials, firestore

# Configurar Firebase
def init_firebase():
    cred = credentials.Certificate({
  "type": "service_account",
  "project_id": "maxdiff-a1891",
  "private_key_id": "802083bf0379f4959459debccebde4b054b36c86",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvwIBADANBgkqhkiG9w0BAQEFAASCBKkwggSlAgEAAoIBAQCdVlUg48SbhHxm\nTqKOsId9gAVQ+GNYN0lnQRHEiT552V8lwIUUFpX9z/IOBwI7CtNCfKgeMbD8SQEl\nnLH2isnNEaaMWFOp0aqq1+0PM2qaLdTAhNgnsXwV2144iUDG6klS1iHOMW3M8JSj\nTDc+L5lh839R6QTorSJF+uO+NVZkOI8dSabxtmB73iMu0rG7iouHeYD8qDG7FdNl\nq34OUL0uHErPKSyrhxRNBnQ210kiTIea3InIiX5kA53n5OrrbfVtXhm++0rjKRAd\nB0nxNMY+mhziHofwA4OLv6bse3c11YgAh4ArxWBIlUU66hs82vOImPYewYNGUdaC\nED9NuB8pAgMBAAECggEASyNpsDVWNXcF+c3f8Aj6C8NRxqN4vi5ZDciTdaqdfY+D\n0wGoDDnlE7t1O6G5PP0kewIRP6o3faRXueClVLpfOWIOicO84MLSoJhSDApgBJWS\nnwZSPFKUkdOboaBaoSRONBMzPcd5SoAyW/IQB9CvjYm96h5AS+YzEfyJOtM6GM3y\nSTGC36Es0vQIU0eVDgoDaBVes6JTwdZjJD3KSRxm0IHaXJ1Bv5zcRQwnfw++igMX\noNWn3TQSjAZL8CEqrGyQNILeOiaG5kpwTNE3FV0rr8ldiAtWEqjrmMgqq+mzY/gq\nXcvEof9Kxr78zcPKbA1FcyRrkY8IwmLlUiVazEr3CQKBgQDJzT+1tJpkrZR6cQCu\nm0wneUlxspN+mBPOUXYnu7Y9bP47O+pYs8J004R2ShK5vDnmvG4U+ivv5ruxV1LV\nMla61j1SfKVBn2SYQdZR5wysoQfC6BwTEcZ1Aj8BuUfe4J88quBYEAlGwGdkW/wD\n4L3Ul/0IfgQonc7Iv3kljrsGewKBgQDHl/Q/+yIyP0FOP/S5FrsAO5f3AS1j6M1F\nVNnapGia5xS2ex6EKYKqOSHUelf9VRQzqFraRe7Xf4xFkeL9QORY/iGOuxuDDMIK\n0GX9I49VEnrdnwwTF1bWFcgjV7YlAWjCNv7N010dIW5aNvwoibVcUKMBfNwXALBn\nJyBYAsPxqwKBgQC//QNVzeLtUa7m5kdt1tWW4G8dOnXUhL6jFSFCH/X7boxYsmH7\nzdl86BcnqsUx639yo2ZfkrrmXC/JQnjN2DxnOJfSuD9ItWow6MIL3bNTMUh/B/Bd\nvBWBEIf9DdbwlecpArC5V1hb9YToGBMlZVV0wry6rZkrQyeOGYwaTTZlrQKBgQCn\nbthNx90i659cBhjEH8ZVZqiPY6RxGH0COTDb0mmR8GGWxueNlMjxBSZU+SDQ+ksN\nHqDAVEQM8Ql53uzc6E/mO6Fo+5sTr2Mj8ThtRyRZCDybp21Yoo6M3w7aXx0EJA9+\nROYxQart4fqRoWiclRDX1Sk4+UYj4ccZcWAXlJJNKwKBgQCXQpfbgjWiwQFqP80g\nc2lQohLuMz0PuyYatMazIH2ZIYiqJeOkvxue0wJi7pAadtI/8dLkqscsVUmbRodl\niYjWOK6DXzUOfnntrzsvuIQOLjAlxZ+5FC7j7wnsxPF4XopTHKupfdVM7CsZRJag\nlh3YZbOZ1Ki4Af9OYt07s+JiKQ==\n-----END PRIVATE KEY-----\n",
  "client_email": "firebase-adminsdk-enu7i@maxdiff-a1891.iam.gserviceaccount.com",
  "client_id": "116262672867032825038",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-enu7i%40maxdiff-a1891.iam.gserviceaccount.com",
  "universe_domain": "googleapis.com"
})  # Reemplaza esta ruta con la ruta de tu archivo JSON
    firebase_admin.initialize_app(cred)

    db = firestore.client()
    return db
