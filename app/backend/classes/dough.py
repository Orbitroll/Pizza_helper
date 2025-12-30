from dataclasses import dataclass, asdict
import json


@dataclass(frozen=True)
class PrefermentSpec:
    name: str
    hydration_pct: float
    idy_pct_of_preferment_flour: float = 0.0
    levain_inoculation_pct: float = 0.0
    salt_pct_of_preferment_flour: float = 0.0

    def to_weights_json(self, total_flour_g: float, preferment_flour_pct: float) -> str:
        pf = total_flour_g * preferment_flour_pct
        water = pf * self.hydration_pct
        idy = pf * self.idy_pct_of_preferment_flour
        levain = pf * self.levain_inoculation_pct
        salt = pf * self.salt_pct_of_preferment_flour

        data = {
            "preferment_name": self.name,
            "flour_g": round(pf, 1),
            "water_g": round(water, 1),
            "idy_g": round(idy, 3),
            "levain_ripe_g": round(levain, 1),
            "salt_g": round(salt, 1),
            "total_preferment_g": round(pf + water + idy + levain + salt, 1)
        }

        return json.dumps(data, ensure_ascii=False, indent=4)

    def to_dict(self, total_flour_g: float, preferment_flour_pct: float):
        pf = total_flour_g * preferment_flour_pct
        water = pf * self.hydration_pct
        idy = pf * self.idy_pct_of_preferment_flour
        levain = pf * self.levain_inoculation_pct
        salt = pf * self.salt_pct_of_preferment_flour

        return {
            "preferment_name": self.name,
            "flour_g": round(pf, 1),
            "water_g": round(water, 1),
            "idy_g": round(idy, 3),
            "levain_ripe_g": round(levain, 1),
            "salt_g": round(salt, 1),
            "total_preferment_g": round(pf + water + idy + levain + salt, 1)
        }


class DoughStarters:
    @staticmethod
    def biga(hydration_pct: float = 0.45, idy_pct_of_preferment_flour: float = 0.001) -> PrefermentSpec:
        return PrefermentSpec("Biga", hydration_pct, idy_pct_of_preferment_flour)

    @staticmethod
    def poolish(hydration_pct: float = 1.0, idy_pct_of_preferment_flour: float = 0.0005) -> PrefermentSpec:
        return PrefermentSpec("Poolish", hydration_pct, idy_pct_of_preferment_flour)

    @staticmethod
    def pate_fermentee(
        hydration_pct: float = 0.6,
        idy_pct_of_preferment_flour: float = 0.001,
        salt_pct_of_preferment_flour: float = 0.02
    ) -> PrefermentSpec:
        return PrefermentSpec("Pâte Fermentée", hydration_pct, idy_pct_of_preferment_flour, 0.0, salt_pct_of_preferment_flour)

    @staticmethod
    def levain(hydration_pct: float = 1.0, levain_inoculation_pct: float = 0.2) -> PrefermentSpec:
        return PrefermentSpec("Levain", hydration_pct, 0.0, levain_inoculation_pct)