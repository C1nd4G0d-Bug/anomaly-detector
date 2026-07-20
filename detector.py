ARCHIVO_LOG = "access.log"

def analizar_logs():
    print(f"[*] Analizando {ARCHIVO_LOG} en busca de anomalías...\n")
    
    intentos_fallidos = {}
    LIMITE_FALLOS = 1

    try:
        with open(ARCHIVO_LOG, "r") as f:
            lineas = f.readlines()
            
            for linea in lineas:
                if "FAILED LOGIN" in linea:
                    ip = linea.strip().split("from ")[1]
                    
                    if ip in intentos_fallidos:
                        intentos_fallidos[ip] += 1
                    else:
                        intentos_fallidos[ip] = 1
                        
                    if intentos_fallidos[ip] > LIMITE_FALLOS:
                        print(f"\033[91m[!!!] ALERTA CRÍTICA: Posible ataque de fuerza bruta desde la IP {ip} ({intentos_fallidos[ip]} intentos)\033[0m")
                    else:
                        print(f"\033[93m[!] Advertencia: Intento fallido aislado desde {ip}\033[0m")
                        
    except FileNotFoundError:
        print("[X] Error: No se encontró el archivo de log.")

if __name__ == "__main__":
    analizar_logs()