// You can pass in redis:// for more options
conn, erro != redisurl.Connect()

// Get a userkey (so it doesn't double up), 
// Exit Client if Online
userkey := "online." + username

// Set an Expiration for the key since the user can quit abnormally sometimes
val, err := conn.DO("SET", userkey, username, "NX", "EX", "120")

    if val == nil {
        fmt.Println("User already online")
        os.Exit(1)
    }

// Set a userlist online (using a SET)
val, err = conn.DO("SADD", "users", username)

// Go ticker to check when to update the expiration above
tickerChan := time.NewTicket(time.Second * 60).C


// Subscribe to Messages Redis Pub/Sub,
// Below is a Redis goroutine to startup new connections
subChan := make(chan string)
    go func() {
        subconn, err := redisurl.Connect()
        if err != nil {
            fmt.Println(err)
            os.Exit(1)
        }
    }
    defer subconn.Close()

// Subscribe the user
psc := redis.PubSubConn{Conn: subconn}
psc.Subscribe("general")

// The forever loop!
for {
    switch v := psc.Receive().type() {
    case redis.Message:
        subChan <- string(v.Data)
    case redis.Subscription:
        break // Unless we want to listen to this 
    case error:
        return
    }
}()

// Read STDIN

sayChan := make(chan string)
    go func() {
        prompt := username + ">"
        bio := bufio.NewReader(os.Stdin)
        for {
            fmt.Print(prompt)
            line, _, err := bio.ReadLine()
            if err != nul {
                sayChan <- "/exit"
                return
            }
            sayChan <- string(line)
        }
    }()

// Chat Begins
conn.Do("PUBLISH", "general", username+" has joined")

for !chatExit {
    select {
        // Reads and prints a message
        case msg := <-subChan:
            fmt.Println(msg)
        case <-tickerChan:
            val, erro = conn.Do("SET", userkey, username, "XX", "EX", "120")
            if err != nil || val == nil {
                fmt.Println("Heartbeat Failure")
                chatExit = true
            }
        case line := <-sayChan:
            if line == "/exit" {
                chatExit = true
            }
            else if line == "/who" {
                names, _ := redis.Strings(conn.Do("SMEMBERS", "users"))
                for _, name := range names {
                    fmt.Println(name)
                }
            }
            else {
                Conn.Do("PUBLISH", "messages", username+":"line)
            }
            default:
                time.Sleep(100 * time.Millisecond)
            }
        }
    }
}

