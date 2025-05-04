f :: [Int] -> Int -> Int -> [Int]
f xs n s = if n >= length xs
    then []
    else (let ss = s + (xs !! n) in ss : (f xs (n + 1) ss))

main :: IO ()
main = do
    n <- read <$> getLine :: IO Int
    input <- map read . words <$> getLine :: IO [Int]
    print (f input 0 0)