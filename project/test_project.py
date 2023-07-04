import project


def test_generate_password():
    assert len(project.generate_password(10, True, True, True, True)) == 10
    assert len(project.generate_password(8, False, True, True, False)) == 8
    assert len(project.generate_password(12, True, False, False, True)) == 12
    assert project.generate_password(6, False, False, False, False) is None


def test_print_password(capsys):
    password = "Abc123!@#"
    project.print_password(password)
    captured = capsys.readouterr()
    assert captured.out.strip() == f"Generated Password: {password}"


def test_assess_strength():
    assert project.assess_strength("Abc123!@#") == "Medium"
    assert project.assess_strength("Pass123") == "Weak"
    assert project.assess_strength("StrongPassword!@#") == "Strong"


def test_print_strength(capsys):
    password = "Abc123!@#"
    project.print_strength(password)
    captured = capsys.readouterr()
    assert captured.out.strip() == "Password Strength: Medium"


def test_main(monkeypatch, capsys):
    inputs = [
        "10",  # length
        "y",   # include lowercase letters
        "y",   # include uppercase letters
        "y",   # include digits
        "y"    # include symbols
    ]
    monkeypatch.setattr('builtins.input', lambda _: inputs.pop(0))

    project.main()

    captured = capsys.readouterr()
    assert captured.out.strip().startswith("Generated Password:")


if __name__ == '__main__':
    test_generate_password()
    test_print_password()
    test_assess_strength()
    test_print_strength()
    test_main()
