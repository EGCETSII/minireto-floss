"""Muestra los paquetes y licencias declaradas de un SBOM SPDX JSON."""
import json
import sys
from pathlib import Path


def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit("Uso: python tools/resumen_sbom.py sbom.spdx.json")
    datos = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    for paquete in datos.get("packages", []):
        print(
            paquete.get("name", "?"),
            paquete.get("versionInfo", "?"),
            paquete.get("licenseDeclared", "NOASSERTION"),
            sep=" | ",
        )


if __name__ == "__main__":
    main()
