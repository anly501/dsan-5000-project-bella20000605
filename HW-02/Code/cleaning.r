# Load the required libraries
library(readxl)
library(dplyr)

# List all data files
data_files <- list.files(path = "./Part2/Data", full.names = TRUE)

#A. Load mental_health data
mental_health_file <- data_files[10] # Assuming mental health data is at index 10
mental_health_df <- read_excel(mental_health_file)
head(mental_health_df)

# Drop columns not related to mental health
mental_health_df <- mental_health_df %>%
  select(-c(`Drug use disorders (%)`, `Alcohol use disorders (%)`))
head(mental_health_df)

# Save the cleaned data to CSV
write.csv(mental_health_df, file = "./Part2/Code/mental_health_r.csv", row.names = FALSE)


# # B.Load eating_disorders data
# eating_disorder_file <- data_files[4] # Assuming eating disorders data is at index 4
# eating_disorder_df <- read.csv(eating_disorder_file)
# head(eating_disorder_df)

# # Drop columns not needed
# eating_disorder_df <- eating_disorder_df %>%
#   select(-c(Continent, `Population (historical estimates)`))
# head(eating_disorder_df)

# # Filter data for years between 1990 and 2021
# eating_disorder_df <- eating_disorder_df %>%
#   filter(Year >= 1990 & Year <= 2021)
# head(eating_disorder_df)

# # Rename columns
# eating_disorder_df <- eating_disorder_df %>%
#   rename(Country = Entity, `Country Code` = Code, Year, Male, Female)
# head(eating_disorder_df)

# # Calculate the mean of Male and Female columns
# eating_disorder_df <- eating_disorder_df %>%
#   mutate(All_gender = rowMeans(.[c("Male", "Female")], na.rm = TRUE))
# head(eating_disorder_df)

# # Save the cleaned data to CSV
# write.csv(eating_disorder_df, file = "./Part2/Code/eating_disorder_r.csv", row.names = FALSE)



#C. Load Countries_Continents data
# countries_continents_file <- data_files[1] # Assuming Countries_Continents data is at index 1
# countries_continents_df <- read.csv(countries_continents_file)
# head(countries_continents_df)

# # Load discomfort_speaking_anxiety_depression_2020 data
# discomfort_data_file <- data_files[2] # Assuming discomfort_speaking_anxiety_depression_2020 data is at index 2
# discomfort_data_df <- read.csv(discomfort_data_file)
# head(discomfort_data_df)

# # Rename columns
# discomfort_data_df <- discomfort_data_df %>%
#   rename(Country, Not_Comfortable = `Share - Question: mh5 - Someone local comfortable speaking about anxiety/depression with someone they know - Answer: Not at all comfortable - Gender: all - Age_group: all`)
# head(discomfort_data_df)

# # Merge the two dataframes
# discomfort_in_continent <- merge(discomfort_data_df, countries_continents_df, by = "Country", all.x = TRUE)
# head(discomfort_in_continent)

# # Save the cleaned data to CSV
# write.csv(discomfort_in_continent, file = "./Part2/Code/discomfort_in_continent_r.csv", row.names = FALSE)
