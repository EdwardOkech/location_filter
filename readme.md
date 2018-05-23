# How to run script
```
$ filter.py <my_outfile.json>
```

#use of script
This script helps me filter out locations by their area names in my day to day job
where i do need to work with locations from a specific country, i do work with large 
json files.At times as large as 20mbs with all locations from a country and a common task is to get 
all locations from a specific region from the original json file.This script helps me filter out the needed locations

#example use
here is an example of the large given json file

```
    {
        "_id": "location:d93f455e-27ca-4408-8c14-e1330917213d",
        "area": "Kumi / Kumi(Kumi)",
        "label": "Aacera"
    },
    {
        "_id": "location:6fd7bf57-f1d7-4a16-adf3-00c07159bc2b",
        "area": "Kumi / Kumi(Kumi)",
        "label": "Aaduka"
    },
    {
        "_id": "location:089c0e3e-571d-4e8c-8d84-c5e72969e7bd",
        "area": "Serere / Kasilo(Serere)",
        "label": "Aarapoo"
    },
    {
        "_id": "location:0f4e64e4-1361-41aa-a7dc-2a67a15eab2b",
        "area": "Koboko / Koboko(Koboko)",
        "label": "Abachi"
    },
    {
        "_id": "location:75087e28-c59f-4e57-a4d9-88d692449411",
        "area": "Apac / Maruzi(Apac)",
        "label": "Abade"
    },
    {
        "_id": "location:da339a30-b84d-4a71-a9b8-32404b3ea926",
        "area": "Lira / Erute(Lira)",
        "label": "Abad Muno"
    },
    {
    "_id": "location:e7be78e5-7327-47cc-b431-d747ca3ba7e6",
    "area": "Kaabong / Dodoth(Kaabong)",
    "label": "Biafra  North"
    }
    truncated
    ----------
```
NOTE::: By truncated i mean the line continues to over 1 million lines of this

Task maybe get all locations from the area Kaabong.
doing this manually is next to impossible remember we have 1 million lines.
To solve this i decided to right this script that when runs should out put something like
OUTPUT:::
```
{
    "_id": "location:0afee9ae-e92b-4a4f-b479-734c18bcc84f",
    "area": "Kaabong / Dodoth(Kaabong)",
    "label": "Apoka"
},{
    "_id": "location:6e21f82b-a8c2-4692-af5c-ec149040bf51",
    "area": "Kaabong / Dodoth(Kaabong)",
    "label": "Army Detach"
},{
    "_id": "location:351ddad1-ad39-4ce1-b7fc-208d7d161d49",
    "area": "Kaabong / Dodoth(Kaabong)",
    "label": "Biafra  East"
},{
    "_id": "location:e7be78e5-7327-47cc-b431-d747ca3ba7e6",
    "area": "Kaabong / Dodoth(Kaabong)",
    "label": "Biafra  North"
},{
    "_id": "location:68417199-c1a4-4428-85c1-9523ad282432",
    "area": "Kaabong / Dodoth(Kaabong)",
    "label": "Biafra  South"
},{
    "_id": "location:547418e7-281e-41d8-b07d-6560c4961381",
    "area": "Kaabong / Dodoth(Kaabong)",
    "label": "Campshahili  North"
}
.....truncated
```
This saves me alot in my day to day tasks

#any contribution to optimise the script is welcome, go ahed and clone it and maybe modify it to fit your needs :)



