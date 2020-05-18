numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1 ]

#https://docs.julialang.org/en/latest/manual/faq/?highlight=splat#...-combines-many-arguments-into-one-argument-in-function-definitions-1
function createphonenumber(numbers)
    return "($(numbers[1:3]...)) $(numbers[4:6]...)-$(numbers[7:10]...)"
end

res = createphonenumber(numbers)

println(res)