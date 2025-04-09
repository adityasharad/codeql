def test(codeql, actions):
    codeql.database.create(source_root="src", verbosity="progress+++")
