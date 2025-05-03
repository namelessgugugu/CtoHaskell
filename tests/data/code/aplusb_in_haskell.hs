main :: IO ()
main = do
    line <- getLine
    let [a, b] = map read (words line) :: [Int]
    print (a + b)