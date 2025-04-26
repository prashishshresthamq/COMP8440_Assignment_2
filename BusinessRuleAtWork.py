import zen
with open("./Assignment_2.json", "r") as f:
  content = f.read()

engine = zen.ZenEngine()

decision = engine.create_decision(content)
result = decision.evaluate({
  "currentTerm": "2025-1",
  "student": {
    "id": 48195472,
    "hasCompleted": "true",
    "academicStanding": "Probation",
    "currentCredits": 18,
    "maxAllowedCredits": 24,
    "expectedGraduationTerm": "2025-2",
    "requiresUnitForGraduation": "true",
    
    "completedUnits": ["COMP1000", "MATH1000"],
    "grades": {
      "COMP1000": "Pass",
      "MATH1000": "Credit"
    }
  },
  "unit": {
    "code": "COMP3000",
    "prerequisites": ["COMP1000", "MATH1000"],
    "schedule": {
      "days": ["Monday", "Wednesday"],
      "time": "11:00-13:00"
    },
    "grade": 75,
    "currentEnrollment": 20,
    "maximumCapacity": 15,
    "availableSpots": 5,
    "creditPoints": 6,
    "isRequiredCore": "true",
    "isHighDemand": "true",
    "enrollmentDeadline": "2025-02-28"
  }
})
print(result)
print("Hello World")