simple = "----. - -. ..--.. ----- ----. ...- ---..  --.. ..--.. --..-- --.- .... -..- -.- ..-  -.--. .--. -.. ..--.-  ..--.- .-. -.-.-. -.. .-.-.- -..- -.-.--  --... .--- -..-. .--.-. .-.. ..... .- -.-- .. -"

function decodemorse(morsecode)
  # your code here 
  tmp = replace(morsecode,r"\+"=>" + ")
  arr = split(tmp,' ')
  filter!(x -> x != "",arr)
    function rpp(x)
        if x == "+"
            return " "
        else
            return x
        end
    end
        
#   res = map(x -> MOR)
  return arr
end

res = decodemorse(simple)

println(res)