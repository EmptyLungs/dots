#! /bin/bash

set -e


(docker events --filter 'event=die' --filter 'event=start' --filter 'event=stop' --filter 'event=restart' --format '{{json .}}' &) | while read event
  do
		action=$( jq -r ".Action" <<< "${event}" )
		image=$( jq -r ".Actor.Attributes.image" <<< "${event}" )
		name=$( jq -r ".Actor.Attributes.name" <<< "${event}")
		
		# if [[ "${image}" -eq 'null' ]]; then
	  #			continue
    #	fi

		dunstify "  ${name}: ${action}" "${image}"
	done

