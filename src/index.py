from varasto import Varasto


def demoa_getterit(varasto: Varasto):
    print(f"saldo = {varasto.saldo}")
    print(f"tilavuus = {varasto.tilavuus}")
    print(f"paljonko_mahtuu = {varasto.paljonko_mahtuu()}")


def demoa_setterit(varasto: Varasto, nimi: str):
    print("Lisätään 50.7")
    varasto.lisaa_varastoon(50.7)
    print(f"{nimi}: {varasto}")
    print("Otetaan 3.14")
    varasto.ota_varastosta(3.14)
    print(f"{nimi}: {varasto}")


def demoa_luonti_virheet():
    print("Varasto(-100.0);")
    huono = Varasto(-100.0)
    print(huono)

    print("Varasto(100.0, -50.7)")
    huono = Varasto(100.0, -50.7)
    print(huono)


def demoa_virhe_lisaykset(varasto: Varasto, nimi: str):
    print(f"{nimi}: {varasto}")
    print("varasto.lisaa_varastoon(1000.0)")
    varasto.lisaa_varastoon(1000.0)
    print(f"{nimi}: {varasto}")
    print("varasto.lisaa_varastoon(-666.0)")
    varasto.lisaa_varastoon(-666.0)
    print(f"{nimi}: {varasto}")


def demoa_virhe_otot(varasto: Varasto, nimi: str):
    print(f"{nimi}: {varasto}")
    print("varasto.ota_varastosta(1000.0)")
    saatiin = varasto.ota_varastosta(1000.0)
    print(f"saatiin {saatiin}")
    print(f"{nimi}: {varasto}")
    print("varasto.otaVarastosta(-32.9)")
    saatiin = varasto.ota_varastosta(-32.9)
    print(f"saatiin {saatiin}")
    print(f"{nimi}: {varasto}")


def main():
    mehua = Varasto(100.0)
    olutta = Varasto(100.0, 20.2)

    print("Luonnin jälkeen:")
    print(f"Mehuvarasto: {mehua}")
    print(f"Olutvarasto: {olutta}")

    print("Olut getterit:")
    demoa_getterit(olutta)

    print("Mehu setterit:")
    demoa_setterit(mehua, "Mehuvarasto")

    print("Virhetilanteita:")
    demoa_luonti_virheet()
    demoa_virhe_lisaykset(mehua, "Mehuvarasto")
    demoa_virhe_otot(olutta, "Olutvarasto")


if __name__ == "__main__":
    main()
