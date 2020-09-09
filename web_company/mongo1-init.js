db.createUser(
    {
        user: "root2",
        pwd:"1234",
        roles: [
            {
                role: "readWrite",
                db:"bar"
            }
        ]
    }
);