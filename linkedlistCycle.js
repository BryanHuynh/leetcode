var deleteDuplicates = function(head) {
    let current = head;
    if(current == null) return null;
    let lastKnown = current;
    
    while(current.next != null){
        //console.log(current.val);
        let succ = current.next;
        if(current.val == succ.val){
            let iter = succ
            if(iter.next == null){
                lastKnown.next = null;
                if(lastKnown.val == current.val){
                    return null;
                }
                return head;
            }
            while(iter.next.val == current.val){
                    iter = iter.next;
                }
                if(lastKnown == current){
                    head = iter.next;
                }else{
                    lastKnown.next = iter.next;
                }
                current = iter.next;
            }

        }else{
            lastKnown = current;
            current = succ;
            
        }
    }
    return head;

};