import json

sampleJson = """{ 
   "class":{ 
      "student":{ 
         "name":"jhon",
         "marks":{ 
            "physics":70,
            "mathematics":80
         }
      }
   }
}"""

print("Checking if nested JSON key exists or not")
sampleDict = json.loads(sampleJson)
if 'marks' in sampleDict['class']['student']:
    print("Student Marks are")
    print("Printing nested JSON key directly")
    print(sampleDict['class']['student']['marks'])