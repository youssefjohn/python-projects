import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
Gray = len(data[data["Primary Fur Color"] == "Gray"])
Cinnamon = len(data[data["Primary Fur Color"] == "Cinnamon"])
Black = len(data[data["Primary Fur Color"] == "Black"])


new_dict = {
    "fur colour": ["Gray", "Cinnamon", "Black"],
    "Count": [Gray, Cinnamon, Black]

}


df = pandas.DataFrame(new_dict)

df.to_csv("new")




