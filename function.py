def list_benefit():
  list_benefit = ["More organized code", "More readable code",
      "Easier code reuse", "Allowing programmers to share and connect code together"
      ]
  return list_benefit

def build_sentence(benefit):
  return "%s is a benefit of functions!" %benefit

def name_of_the_benefit_of_function():
  list_of_benefits = list_benefit()
  for benefit in list_of_benefits:
    print build_sentence(benefit)

name_of_the_benefit_of_function();
