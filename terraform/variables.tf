variable "resource_group_name" {
  description = "The name of the Azure Resource Group"
  default     = "iot_project_rg"
}

variable "location" {
  description = "Azure region where resources will be deployed"
  default     = "South India"
}

variable "eventhub_namespace" {
  description = "Event Hub Namespace name"
  default     = "iot-eventhub-unique"
}

variable "iothub_name" {
  description = "IoT Hub name"
  default     = "iot-hub-banu"
}

variable "log_analytics_name" {
  description = "Log Analytics Workspace name"
  default     = "iot-logs"
}

variable "asa_job_name" {
  description = "Azure Stream Analytics Job name"
  default     = "iot-stream"
}

variable "adx_name" {
  description = "Azure Data Explorer Cluster name"
  default     = "dataexplorerforgrafana"
}

variable "storage_account_name" {
  description = "Azure Storage Account name"
  default     = "iotadlsstorage"
}
