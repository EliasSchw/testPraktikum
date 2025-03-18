import LinearDataCalculator as ldc




slope = ldc.calculate_slope_from_csv("./TestdataLinear.CSV")
print(f"The slope of the best-fit line is: {slope}")