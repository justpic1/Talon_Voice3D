**Plan for RPC**
```
{
    command: {
        name: [command]
        specifiers: {
            target_list:{
                [a]: {
                    descriptors:{
                    }
                }
                [b]: {
                    descriptors:{
                    }
                }
            }
            |destination|: {
                |prep|: [x] (to)
                target: [a]
            }
        }
    }
}
```
```
command: name
target1: descriptor1 - descriptor2... | target2...
destination: prep | target
```