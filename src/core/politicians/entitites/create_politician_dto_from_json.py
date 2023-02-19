from core.politicians.entitites.politicians import CreatePoliticianDto
from shared.convert import optional_comma_float


def create_politician_dto_from_json(json_dict: dict):
    json_dict = {key.lower(): json_dict[key] for key in json_dict}
    for float_key in [
        "sueldobase_sueldo",
        "complementos_sueldo",
        "pagasextra_sueldo",
        "otrasdietaseindemnizaciones_sueldo",
        "trienios_sueldo",
        "retribucionmensual",
        "retribucionanual",
    ]:
        json_dict[float_key] = optional_comma_float(json_dict[float_key])
    return CreatePoliticianDto(**json_dict)
