from typing import Optional

from pydantic import BaseModel


class CreatePoliticianDto(BaseModel):
    nombre: str
    partido: str
    partido_para_filtro: str
    genero: str
    cargo_para_filtro: str
    cargo: str
    institucion: str
    ccaa: str
    sueldobase_sueldo: Optional[float]
    complementos_sueldo: Optional[float]
    pagasextra_sueldo: Optional[float]
    otrasdietaseindemnizaciones_sueldo: Optional[float]
    trienios_sueldo: Optional[float]
    retribucionmensual: Optional[float]
    retribucionanual: Optional[float]
    observaciones: str


class UpdatePoliticianDto(BaseModel):
    nombre: Optional[str]
    partido: Optional[str]
    partido_para_filtro: Optional[str]
    genero: Optional[str]
    cargo_para_filtro: Optional[str]
    cargo: Optional[str]
    institucion: Optional[str]
    ccaa: Optional[str]
    sueldobase_sueldo: Optional[float]
    complementos_sueldo: Optional[float]
    pagasextra_sueldo: Optional[float]
    otrasdietaseindemnizaciones_sueldo: Optional[float]
    trienios_sueldo: Optional[float]
    retribucionmensual: Optional[float]
    retribucionanual: Optional[float]
    observaciones: Optional[str]


class Politician(BaseModel):
    id: str
    nombre: str
    partido: str
    partido_para_filtro: str
    genero: str
    cargo_para_filtro: str
    cargo: str
    institucion: str
    ccaa: str
    sueldobase_sueldo: Optional[float]
    complementos_sueldo: Optional[float]
    pagasextra_sueldo: Optional[float]
    otrasdietaseindemnizaciones_sueldo: Optional[float]
    trienios_sueldo: Optional[float]
    retribucionmensual: Optional[float]
    retribucionanual: Optional[float]
    observaciones: str

    class Config:
        extra = "ignore"
