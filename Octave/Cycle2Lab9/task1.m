
fprintf("Task 1")

function str2vector (st)

  st= tolower(st);
  m = length(st);
  for i = 1:256
	  freq(i) =0;
  endfor
  for i = 1:m
	    c = st(i);
            if(isletter(c))
	      freq(c) = freq(c)+1;
            endif 
  endfor
	    disp(freq())
 endfunction

 str2vector("Hello Programming Languages Lab!")
 

