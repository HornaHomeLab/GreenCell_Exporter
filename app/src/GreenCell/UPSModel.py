from pydantic import BaseModel, Field


class UPSStatus(BaseModel):
    ip: str
    InputVoltage: float = Field(alias="inputVoltage")
    InputVoltageFault: float = Field(alias="inputVoltageFault")
    OutputVoltage: float = Field(alias="outputVoltage")
    Load: float = Field(alias="load")
    InputFrequency: float = Field(alias="inputFrequency")
    BatteryVoltage: float = Field(alias="batteryVoltage")
    Temperature: float | None = Field(alias="temperature")
    UtilityFail: bool = Field(alias="utilityFail")
    BatteryLow: bool = Field(alias="batteryLow")
    BypassBoost: bool = Field(alias="bypassBoost")
    Failed: bool = Field(alias="failed")
    Offline: bool = Field(alias="offline")
    TestInProgress: bool = Field(alias="testInProgress")
    ShutdownActive: bool = Field(alias="shutdownActive")
    BeeperOn: bool = Field(alias="beeperOn")
    BatteryLevel: float = Field(alias="batteryLevel")
    Active: bool = Field(alias="active")
    Connected: bool = Field(alias="connected")
    Status: int = Field(alias="status")
    Register: list[str] = Field(alias="register")
    Issues: list[str] = Field(alias="issues")
    Errno: int = Field(alias="errno")
    InputVoltageNominal: float = Field(alias="inputVoltageNominal")
    InputFrequencyNominal: float = Field(alias="inputFrequencyNominal")
    BatteryVoltageNominal: float = Field(alias="batteryVoltageNominal")
    InputCurrentNominal: float = Field(alias="inputCurrentNominal")
    BatteryNumberNominal: float = Field(alias="batteryNumberNominal")
    BatteryVoltageHighNominal: float = Field(alias="batteryVoltageHighNominal")
    BatteryVoltageLowNominal: float = Field(alias="batteryVoltageLowNominal")
    Reg: int = Field(alias="reg")
