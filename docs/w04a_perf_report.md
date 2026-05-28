# W04A - Reporte de Performance

**Timestamp:** 2026-05-28T19:22:18.665793+00:00

## Tablas
| Tabla | Filas |
|-------|-------|
| fact_planet | 6286 |
| dim_host_full | 4705 |

## Consulta analizada
```sql
SELECT 
    h.hostname,
    h.st_teff,
    COUNT(f.pl_name) AS n_planets,
    AVG(f.pl_rade) AS avg_radius
FROM fact_planet f
JOIN dim_host_full h ON f.hostname = h.hostname
GROUP BY h.hostname, h.st_teff
ORDER BY n_planets DESC
```

## Plan de ejecucion
Guardado en: `w04a_explain_q.txt`

---
*Generado automaticamente*