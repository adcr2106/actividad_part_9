from typing import Dict, Any


class AnalizadorLogs:
    def __init__(self, nombre_archivo: str):
        self.nombre_archivo = nombre_archivo

    def procesar_logs(self) -> Dict[str, Any]:
        solicitudes_por_metodo = {}
        solicitudes_por_codigo = {}

        tamano_total_respuesta = 0
        numero_solicitudes = 0

        solicitudes_por_url = {}

        with open(self.nombre_archivo, "r") as archivo:
            for linea in archivo:
                datos = linea.strip().split(" ")
                if len(datos) < 6:
                    continue

                ip, fecha_hora, metodo, url, codigo_respuesta, tamano_respuesta = datos

                if metodo in solicitudes_por_metodo:
                    solicitudes_por_metodo[metodo] += 1
                else:
                    solicitudes_por_metodo[metodo] = 1

                if codigo_respuesta in solicitudes_por_codigo:
                    solicitudes_por_codigo[codigo_respuesta] += 1
                else:
                    solicitudes_por_codigo[codigo_respuesta] = 1

                tamano_total_respuesta += int(tamano_respuesta)
                numero_solicitudes += 1

                if url in solicitudes_por_url:
                    solicitudes_por_url[url] += 1
                else:
                    solicitudes_por_url[url] = 1

        if numero_solicitudes > 0:
            tamano_promedio_respuesta = tamano_total_respuesta / numero_solicitudes
        else:
            tamano_promedio_respuesta = 0

        urls_mas_solicitadas = sorted(solicitudes_por_url.items(), key=lambda x: x[1], reverse=True)[:10]

        estadisticas = {
            "total_solicitudes": numero_solicitudes,
            "solicitudes_por_metodo": solicitudes_por_metodo,
            "solicitudes_por_codigo": solicitudes_por_codigo,
            "tamano_total_respuesta": tamano_total_respuesta,
            "tamano_promedio_respuesta": tamano_promedio_respuesta,
            "urls_mas_solicitadas": dict(urls_mas_solicitadas)
        }

        return estadisticas

analizador = AnalizadorLogs('trafico_web.log')
estadisticas = analizador.procesar_logs()
print(estadisticas)

