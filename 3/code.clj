(ns trees)

(def land (slurp "trees.txt"))
(def lanes (clojure.string/split-lines land))

(def earth
  (for [lane lanes]
    (apply str (repeat (quot (count lanes) (count lane)) lane))))

(def world (atom {}))
(def grid
  (doseq [y (range (count earth))]
    (doseq [x (range (count (get (vec earth) y)))]
      (swap! world assoc [x y] (get (vec (get (vec earth) y)) x)))))
