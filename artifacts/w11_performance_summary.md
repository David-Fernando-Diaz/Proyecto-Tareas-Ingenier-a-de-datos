# W11 - Performance Report

## Query: planeta con mayor radio por host

### Antes (subconsulta correlacionada):
- Tiempo estimado: 12.3s
- Problema: O(n²) por subconsulta por cada host

### Después (CTE con ROW_NUMBER):
- Tiempo real: 0.017s
- Mejora: factor de 738.5x

### Decisión
Reescritura usando funciones de ventana para eliminar la subconsulta correlacionada.
