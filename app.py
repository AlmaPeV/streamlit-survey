import gspread
from google.oauth2.service_account import Credentials

# Autenticación con las credenciales de servicio
# Asegúrate de que la ruta esté correcta hacia el archivo JSON de credenciales en tu repositorio
creds = Credentials.from_service_account_file('.devcontainer/encuesta-ko-b5e41359ea53.json')
client = gspread.authorize(creds)

# Abrir la hoja de cálculo (Google Sheets)
spreadsheet = client.open_by_key("14MFsN9xYS1EbLWEXq3g6pp4UQ6Fyy2cdsbDdOmcjCDU")


# Ejemplo de cómo añadir una fila de datos
sheet.append_row(["Nombre del participante", "Muestra seleccionada", "Ronda"])
import gspread
