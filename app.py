import gspread
from google.oauth2.service_account import Credentials

# Configura el alcance
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]

# Carga las credenciales
creds = Credentials.from_service_account_file('.devcontainer/encuesta-ko-b5e41359ea53.json', scopes=scope)
client = gspread.authorize(creds)

# Abrir la hoja de cálculo (Google Sheets)
spreadsheet = client.open_by_key("14MFsN9xYS1EbLWEXq3g6pp4UQ6Fyy2cdsbDdOmcjCDU")


# Ejemplo de cómo añadir una fila de datos
sheet.append_row(["Nombre del participante", "Muestra seleccionada", "Ronda"])
import gspread

