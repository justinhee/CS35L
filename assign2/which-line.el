
(defun which-line ()
  "Print the current line number (in the buffer) of point and the total number of lines in the buffer."
  (interactive)
  (save-restriction
    (widen)
    (save-excursion
      (beginning-of-line)
      (let ((numLines (if (= (point-min) (point-max)) 0 (if (= 10 (char-before (point-max))) (count-lines 1 (point-max)) (- (count-lines 1 (point-max)) 1)))))
	(message "Line %d of %d" (line-number-at-pos) numLines)))))
