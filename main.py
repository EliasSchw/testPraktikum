import LinearDataCalculator as ldc


c = ldc.LinearDataCalculator()

slope = c.calculate_slope_from_csv("./TestdataLinear.CSV")
print(f"The slope of the best-fit line is: {slope}")
