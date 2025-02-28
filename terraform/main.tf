resource "azurerm_resource_group" "iot_rg" {
  name     = var.resource_group_name
  location = var.location
}

resource "azurerm_eventhub_namespace" "eventhub" {
  name                = var.eventhub_namespace
  location            = azurerm_resource_group.iot_rg.location
  resource_group_name = azurerm_resource_group.iot_rg.name
  sku                = "Standard"
  capacity           = 2
}
