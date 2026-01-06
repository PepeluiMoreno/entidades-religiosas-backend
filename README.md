# Registro de Entidades Religiosas (RER) - España

## Descripción
Este proyecto implementa un backend para gestionar el **Registro de Entidades Religiosas (RER)** de España. Permite almacenar y consultar información sobre iglesias, confesiones, comunidades, federaciones y fundaciones religiosas inscritas oficialmente.

## Características
- **Versionado Temporal (SCD Tipo 2)**: Seguimiento histórico de cambios en las entidades.
- **ETL Automatizada**: Proceso de carga incremental desde fuentes oficiales.
- **Integración Geográfica**: Preparado para filtrado por Comunidad, Provincia y Municipio.

## Fuentes de Datos
- **Ministerio de Justicia**: [Buscador de Entidades Religiosas](https://maper.mjusticia.gob.es/Maper/RER.action).
- **Datos.gob.es**: [Dataset de Entidades Religiosas](https://datos.gob.es/es/catalogo/e00003901-entidades-religiosas).

## Instalación y Uso
1. Configurar `DATABASE_URL` en el entorno.
2. Ejecutar la ETL: `python app/etl/etl_process.py`.
3. Integrar como módulo en proyectos GraphQL para consultas unificadas.
