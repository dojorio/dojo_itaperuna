require "../fizzbuzz.rb"

describe "Teste do FizzBuzz" do

	it "com o numero 3 deve retornar fizz" do
		fizzbuzz(3).should == "fizz"
  end

  it "com o numero 5 deve retornar buzz" do
    fizzbuzz(5).should == "buzz"
	end

	it "com o numero 15 deve retornar fizzbuzz" do
		fizzbuzz(15).should == "fizzbuzz"
	end

	it "com o numero 30 deve retornar fizzbuzz" do
		fizzbuzz(30).should == "fizzbuzz"	
	end

	it "com o numero 45 deve retornar fizzbuzz" do
	   fizzbuzz(45).should == "fizzbuzz"
	end

	it "com o numero 37 não deve retornar nada" do
		fizzbuzz(37).should == ""
  end

	it "com o numero 60 deve retornar fizzbuzz" do
		fizzbuzz(60).should == "fizzbuzz"
	end

	it "com o numero 75 deve retornar fizzbuzz" do
		fizzbuzz(75).should == "fizzbuzz"
	end
end
