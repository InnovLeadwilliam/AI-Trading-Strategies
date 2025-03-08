# 📈 Estrategia de Trading Algorítmico con QuantConnect
# Implementamos una estrategia basada en el cruce de medias móviles.

from AlgorithmImports import *

class MovingAverageCrossAlgorithm(QCAlgorithm):
    def Initialize(self):
        self.SetStartDate(2020, 1, 1)  # Fecha de inicio del backtest
        self.SetEndDate(2024, 1, 1)    # Fecha de finalización del backtest
        self.SetCash(10000)            # Capital inicial

        # Seleccionar activo
        self.asset = self.AddEquity("AAPL", Resolution.Daily).Symbol

        # Definir indicadores
        self.short_mavg = self.SMA(self.asset, 10, Resolution.Daily)
        self.long_mavg = self.SMA(self.asset, 50, Resolution.Daily)

    def OnData(self, data):
        if not self.short_mavg.IsReady or not self.long_mavg.IsReady:
            return

        # Estrategia de cruce de medias móviles
        if self.short_mavg.Current.Value > self.long_mavg.Current.Value:
            self.SetHoldings(self.asset, 1)  # Comprar
        elif self.short_mavg.Current.Value < self.long_mavg.Current.Value:
            self.SetHoldings(self.asset, 0)  # Vender
