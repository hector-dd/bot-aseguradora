import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = [
"https://spreadsheets.google.com/feeds",
"https://www.googleapis.com/auth/drive"
]

creds = ServiceAccountCredentials.from_json_keyfile_name(
"credentials.json", scope
)

client = gspread.authorize(creds)

sheet = client.open("polizas").sheet1

data = sheet.get_all_records()


def buscar_cliente(nombre):

    nombre = nombre.lower()

    resultados = []

    for row in data:

        full = f"{row['nombre']} {row['apellido_p']} {row['apellido_m']}".lower()

        if nombre in full:
            resultados.append(row)

    return resultados