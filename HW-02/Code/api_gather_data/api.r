# Define the API endpoint URL
library(httr)
library(jsonlite)
url <- "https://datacatalogapi.worldbank.org/ddhxext/ResourceFileData?resource_unique_id=DR0090755&version_id=2023-09-27T16:44:25.8023254Z"

# Make the GET request
response <- GET(url)
response.text <- content(response, "text")

data <- fromJSON(response.text)
data
details <- data$Details

# To write this data to a CSV file
write.csv(details, file = './api_r.csv', row.names = FALSE)

