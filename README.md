# TASK 1: Software Cofiguration

## Subtask 1: Why did I choose to participate in the Dare IT Challenge?

<br>

> Little by little a little becomes a lot.
> <br> <b><p align="right">Tanzanian proverb</p></b>

My name is <b>Dmytro</b>. I've been working as a teacher at a primary school and currently, I am in the middle of changing my career path. I have tried to find work as a manual tester, but it was not as easy as I had expected.<br><br>
That is why I decided to take part in the <b>Dare IT Challenge</b>, because I believe that skills in test automation will help me find my first job.<br><br>
In addition, I hope that I will meet interesting people who I will have kept in touch with even after the course ends.
<br><br>

# TASK 2: Selectors

1. <b>Scouts Panel</b> title

- `//h5[@class='MuiTypography-root MuiTypography-h5 MuiTypography-gutterBottom']`
- `//div[@id='__next']/form/div/div[1]/h5`
- `//h5`
- `//*[text()="Scouts Panel"]`
  <br><br>

2. <b>Login</b> input field

- `//input[@id='login']`
- `//input[@name='login']`
- `/html/body/form/div/div[1]/div[1]/div/input`
  <br><br>

3. <b>Password</b> input field

- `//input[@id='password']`
- `//input[@name='password']`
- `//label[@id='password-label']/../div/input`
  <br><br>

4. <b>Remind password</b> hyperlink

- `//*[text()="Przypomnij hasło"]`
- `//a`
- `//div[@id='__next']/form/div/div[1]/a`
  <br><br>

5. <b>Select language</b> dropdown button

- `//div[@id='__next']/form/div/div[2]/div/div`
- `//div[@aria-haspopup='listbox']`
- `//*[text()="Polski" or text()="English"]`
  <br><br>

6. <b>SIGN IN</b> button

- `//button`
- `//*[@type='submit']`
- `//*[@id='__next']/form/div/div[2]/button`
