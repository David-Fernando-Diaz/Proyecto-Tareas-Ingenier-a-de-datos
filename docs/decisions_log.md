# Decisions Log

- Fecha: 2026-05-28
- Decisión: Guardar SHA-256 del CSV raw en artifacts por cada ejecución.
- Razón: Detectar cambios invisibles del dato (DDIA reliability/operability). Además, se añadió un check de duplicados para garantizar la unicidad de pl_name.
- Alternativas: Confiar en el nombre del archivo (rechazada), usar solo fecha de descarga (rechazada).
- Evidencia: raw_sha256=cd30dfbf742ac71ee69a7e24d6ac80f9e4126bf7e2bb9d46844637761e75a5a8, n_rows=6291, n_cols=84, duplicate_count=0

