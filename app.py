import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Definir el alcance de los permisos (Google Sheets y Google Drive)
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]

# Autenticación con las credenciales de servicio
# Asegúrate de que la ruta esté correcta hacia el archivo JSON de credenciales en tu repositorio
creds = ServiceAccountCredentials.from_json_keyfile_name('.devcontainer/encuesta-ko-2b99bdde8769.json', scope)
client = gspread.authorize(creds)

# Abrir la hoja de cálculo (Google Sheets)
spreadsheet = client.open("SURVEY-KO")
sheet = spreadsheet.sheet1  # Si tienes más de una hoja, puedes seleccionar la primera con sheet1

# Ejemplo de cómo añadir una fila de datos
sheet.append_row(["Nombre del participante", "Muestra seleccionada", "Ronda"])
