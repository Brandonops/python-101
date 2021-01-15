ramit = {
    "name": "Ramit",
    "email": "ramit@gmail.com",
    "interests": ["movies","tennis"],
    "friends" : [
        {
            "name": "Jasmine",
            "email": "jasmine@yahoo.com",
            "interests": ["photography", "tennis"]
        },
{
            "name": "Jan",
            "email": "jan@hotmail.com",
            "interests": ["movies", "tv"]
}
    ]
}

email_of_ramit = ramit["email"]
ramit_first_interest = ramit["interests"][0]
print("Ramit's email: " + email_of_ramit, "| Ramit's first interest: " + ramit_first_interest)

email_of_jasmine = ramit["friends"][0]["email"]
jasmine_second_interest = ramit["friends"][0]["interests"][1]

print("Jasmine's email: " + email_of_jasmine, "| Jasmine's second interest: " + jasmine_second_interest)
