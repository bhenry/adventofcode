(ns trees)

(def land (slurp "trees.txt"))
(def lanes (clojure.string/split-lines land))

(def earth
  (for [lane lanes]
    (apply str (repeat (quot (count lanes) (count lane)) lane))))

(def world (atom {}))
(def grid
  (doseq [[y row] (map-indexed vector earth)]
    (doseq [[x col] (map-indexed vector row)]
      (swap! world assoc [x y] col))))

(print (get @world [7 1]))
(print (get @world [5 1]))
